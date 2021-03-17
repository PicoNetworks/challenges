export default function Form() {
    const registerUser = async (event) => {
        event.preventDefault()

        const res = await fetch('/api/register', {
            body: JSON.stringify({
                name: event.target.name.value,
            }),
            headers: {
                'Content-Type': 'application/json',
            },
            method: 'POST',
        })

        const result = await res.json()
        return result
        // result.user => 'Ada Lovelace'
    }

    return (
        <form onSubmit={registerUser}>
            <label htmlFor="name">
                Name
                <input id="name" name="name" type="text" autoComplete="name" required />
            </label>
            <button type="submit">Register</button>
        </form>
    )
}
