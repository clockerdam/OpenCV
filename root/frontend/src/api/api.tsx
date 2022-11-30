let endpoint = process.env.REACT_APP_API_ENDPOINT

async function uploadUnlabeled(resume: string) {
    const response = await fetch(endpoint + "/unlabeled", {
        method: "POST",
        body: resume,
        headers: { 'Content-Type': 'application/json' }
    })
    return response
}

async function labelCV(resume: string) {
    const response = await fetch(endpoint + "/label", {
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

async function getAnalysis(resume: string) {
    const response = await fetch(endpoint + "/analysis", {
        method: "POST",
        body: resume,
        headers: { 'Content-Type': 'application/json' }
    })
    console.log(response)
    return response.json()
}

export { uploadUnlabeled,labelCV, getUnlabeled, getAnalysis}



