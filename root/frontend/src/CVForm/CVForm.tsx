import { FormEvent, useState } from "react";
import './cvForm.css'

// https://www.freecodecamp.org/news/build-dynamic-forms-in-react/
function CVForm() {
    const [state, setState] = useState({
        title: '',
        summary: '',
        interests: ['']

    })

    const addInterest = () => {
        let newInterest = ''

        let data = state.interests
        data.push(newInterest)

        setState(prevState => ({...prevState, interests: data}))
    }

    return <form onSubmit={handleSubmit}>
        <div>
            <label>
                Title
                <input 
                    name="title"
                    placeholder="Title"
                    value={state.title}
                    onChange={(e) => setState(prevState => ({ ...prevState, title: e.target.value }))}
                />
            </label>
            <label>
                Summary
                <input 
                    name="summary"
                    placeholder="Summary"
                    value={state.summary}
                    onChange={(e) => setState(prevState => ({ ...prevState, summary: e.target.value }))}
                />
            </label>
            <label>
                Interests
                {state.interests.map((interest, index) => {
                return (<div key={index}>
                        <input
                            name="interest"
                            placeholder="Interest"
                            value={interest}
                            onChange={e => handleInterestChange(index, e)}
                        />
                    </div>)
                })}
                <button onClick={addInterest}>Add interest</button>
            </label>
            
            <button type="submit">Submit CV</button>
        </div>
    </form>

    function handleSubmit(e: FormEvent) {
        e.preventDefault()
        console.log(state)
    }

    function handleInterestChange(index: number, event: any) {
        let data = [...state.interests]
        data[index] = event.target.value
        setState(prevState => ({...prevState, interests: data}))
    }
}

export { CVForm }