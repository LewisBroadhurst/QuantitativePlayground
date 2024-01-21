import { io } from "socket.io-client";

export default function StreamingPanel() {

    const url = import.meta.env.VITE_OANDA_FXPRACTISE_STREAM_URL;
    const accountId = import.meta.env.VITE_OANDA_FXPRACTISE_ACCOUNT_ID;

    function handleStreamClick() {
        // Have funtionality to understand if stream is already running

        const x = fetch(`${url}/accounts/${accountId}/pricing/stream?instruments=EUR_USD`, {
            method: "GET",
            headers: new Headers({
                "Authorization": `Bearer ${import.meta.env.VITE_OANDA_API_KEY}`,
                "Content-Type": "application/octet-stream"
            })
        })
            .then(res => res.body)
            .then(body => {
                // @ts-ignore
                const reader = body.getReader();
                console.log(reader)
                return new ReadableStream({
                    start(controller) {
                        function push() {
                            // "done" is a Boolean and value a "Uint8Array"
                            reader.read().then(({ done, value }) => {
                                // If there is no more data to read
                                if (done) {
                                    console.log("done", done);
                                    controller.close();
                                    return;
                                }
                                // Get the data and send it to the browser via the controller
                                controller.enqueue(value);
                                // Check chunks by logging to the console
                                console.log(done, value);

                                console.log(JSON.stringify(value), JSON.parse(JSON.stringify(value)));

                                push();
                            });
                        }

                        push();
                    }


                })
            })
            .then((stream) =>
                // Respond with our stream
                new Response(stream, { headers: { "Content-Type": "text/html" } }).text(),
            )
            .then((result) => {
                // Do things with result
                console.log(result);
            })

        console.log(x);
    }

    return <section className="p-4 bg-slate-50 flex flex-col gap-4" >
        <h1 className="text-2xl underline">Streaming Panel</h1>

        <section>

        </section>

        <button
            className="bg-blue-500 text-white px-4 py-2 rounded-sm self-start"
            onClick={handleStreamClick}
        >
            Start Stream
        </button>
    </section >
}