from fastapi import APIRouter,HTTPException
from app.schemas.translation import TranslatedPayload
from app.services.file_services import (
    save_translation,
    read_translation,
    delete_translations
)

router =APIRouter(prefix="/translations",tags=["Translations"])


### Api for the translations


# @router.post("/")
# def upload_translations(payload:TranslationPayload):
#     print("payload",payload)
#     save_translation(payload.dict())
#     return {
#         "status":"success",
#         "message":"Translation file is moved succesfully"
#     }
@router.post("/")
def upload_translations(payload: TranslatedPayload):
    try:
        save_translation(payload.model_dump())

        return {
            "project_name": payload.project_name,
            "languages": payload.languages,
            "message": "Translation file saved successfully"
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "data": {
                    "message": "Failed to save translation file",
                    "reason": str(exc)
                }
            }
        )


@router.get("/")
def get_translation():
    try:
        data = read_translation()

        if not data:
            raise HTTPException(
                status_code=404,
                detail={
                    "status": "error",
                    "data": {
                        "message": "No translation keys found"
                    }
                }
            )

        return {
            "status": "success",
            "data": data
        }

    except HTTPException:
        raise

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "data": {
                    "message": "Failed to read translation file",
                    "reason": str(exc)
                }
            }
        )


@router.delete("/")
def delete_translation():
    try:
        delete_translations()

        return {
            "status": "success",
            "data": {
                "message": "Translation data deleted successfully"
            }
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "data": {
                    "message": "Failed to delete translation data",
                    "reason": str(exc)
                }
            }
        )