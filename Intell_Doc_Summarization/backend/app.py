from fastapi import (
    FastAPI,
    UploadFile,
    File
)

from fastapi.middleware.cors import (
    CORSMiddleware
)

from pdf_reader import (
    extract_text
)

from summarizer import (
    generate_summary
)


app = FastAPI()


app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_methods=["*"],

    allow_headers=["*"]

)


@app.post(
    "/summarize"
)

async def summarize(

    file: UploadFile = File(...)

):

    # Extract text
    text = extract_text(
        file.file
    )


    if not text:

        return {

            "error":
                "Invalid PDF"

        }


    # Generate summary
    summary = generate_summary(
        text
    )


    return {

        "summary":
            summary,

        "original_words":
            len(
                text.split()
            ),

        "summary_words":
            len(
                summary.split()
            )

    }