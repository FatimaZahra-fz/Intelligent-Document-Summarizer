async function uploadFile(){

    const file =
        document.getElementById("pdfFile").files[0];

    let formData = new FormData();

    formData.append("file", file);

    document.getElementById(
        "result"
    ).innerText = "Processing...";


    const response = await fetch(
        "http://127.0.0.1:8000/summarize",
        {
            method: "POST",
            body: formData
        }
    );

    const data = await response.json();


    if(data.error){

        document.getElementById(
            "result"
        ).innerText = data.error;

        return;
    }


    document.getElementById(
        "result"
    ).innerText = data.summary;


    document.getElementById(
        "originalCount"
    ).innerText = data.original_words;


    document.getElementById(
        "summaryCount"
    ).innerText = data.summary_words;

}