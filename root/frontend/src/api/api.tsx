let port = 8080
let endpoint = "http://localhost:" + port

async function uploadUnlabeled(resume: string) {
    const response = await fetch(endpoint + "/unlabeled", {
        method: "POST",
        body: resume,
        headers: { 'Content-Type': 'application/json' }
    })
    return response
}

export { uploadUnlabeled }


