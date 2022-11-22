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

async function getUnlabeled() {
    const response = await fetch(endpoint + "/unlabeled")  
    return await response.json()
}

async function getAnalysis() {
    const response = await fetch(endpoint + "/labeled")  
    return await response.json()
}

export { uploadUnlabeled, getUnlabeled, getAnalysis}



