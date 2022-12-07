import { CV } from "../CV/CV"

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

async function getPdfData(resume: CV): Promise<string> {
  // Returns the Base64 encoded pdf for the provided CV
  let res = await fetch(endpoint + "/generate", {
    method: "POST",
    body: JSON.stringify(resume),
    headers: { 'Content-Type': 'application/json' }
  })

  let blob = await res.blob()
  var reader = new FileReader();
  reader.readAsDataURL(blob);

  return new Promise((resolve, reject) => {

    reader.onload = (ev) => {
      let val = ev?.target?.result;

      if (val) {
        resolve(val as string)
      } else {
        reject();
      }
    }
  })
}

export { uploadUnlabeled, labelCV, getUnlabeled, getAnalysis, getPdfData }



