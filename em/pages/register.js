export default function Form() {
    const registerUser = async (event) => {
        event.preventDefault()

        // TODO: this should use pipedream instead
        // WTF is this?? why fetch? this is 2021.
        // commenting out for now
        // const res = await fetch('/api/register', {
        //     body: JSON.stringify({
        //         name: event.target.name.value,
        //     }),
        //     headers: {
        //         'Content-Type': 'application/json',
        //     },
        //     method: 'POST',
        // })

        const res = await fetch(
            'https://enx2y83d8t3c9.x.pipedream.nett/',
            {
              body: JSON.stringify({
                name: event.target.name.value
              }),
              headers: {
                'Content-Type': 'application/json'
              },
              method: 'POST'
            }
          )

        const result = await res.json();
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
