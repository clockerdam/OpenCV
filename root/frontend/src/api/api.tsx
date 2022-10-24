import { CV } from "./cv"

let port = 8080
let endpoint = "http://localhost:" + port

async function cvUpload(cv?: CV) {
    const response = await fetch(endpoint + "/cvupload", {
        method: "POST",
        body: JSON.stringify(cv),
        headers: { 'Content-Type': 'application/json' }
    })
    return response
}

export { cvUpload }



