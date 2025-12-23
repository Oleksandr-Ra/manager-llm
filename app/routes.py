from fastapi import APIRouter, HTTPException
from llm_manager import llm_factory
from llm_schemas import GenerationRequest, GenerationResponse

router = APIRouter()


@router.post("/generate", response_model=GenerationResponse)
async def generate_text(request: GenerationRequest):
    try:
        client = llm_factory.get_client(name=request.client_name)
        result = await client.generate(
            prompt=request.prompt,
            temperature=request.temperature,
        )
        return GenerationResponse(result=result)

    except ValueError as e:
        # Error if client not found or not configured
        raise HTTPException(status_code=400, detail=str(e)) from e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e
