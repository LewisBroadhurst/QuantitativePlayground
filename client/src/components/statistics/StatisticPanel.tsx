import { useEffect, useState } from "react"

// type PolygonPreviousClose = {
//     adjusted: true,
//     queryCount: number,
//     requestId: string,
//     results: [],
//     resultsCount: number,
//     status: string,
//     ticker: string,
// }

// AAPL, TSLA, NVDA, AMZN, GOOG, FB, MSFT, PYPL, NFLX, ADBE, CRM, PFE

export default function StatisticPanel() {

    const [ticker, setTicker] = useState<string>("AAPL");
    const [statistics, setStatistics] = useState();

    useEffect(() => {
        fetch(`https://api.polygon.io/v2/aggs/ticker/${ticker}/prev?adjusted=true&apiKey={process.env.POLYGON_API_KEY}`)
            .then(res => res.json())
            .then(data => setStatistics(data))
            .catch(err => console.error(err))
    }, [])


    return <article className="flex flex-col gap-10 p-4 bg-slate-100">
        <h1 className="text-2xl underline">Statistics</h1>

        <section className="flex flex-col gap-1 w-40">
            <span>Current Ticker: {ticker}</span>
            <div className="flex flex-row gap-4">
                <input className="rounded-sm" type="text" placeholder="e.g TSLA" onChange={(e) => setTicker(e.target.value)} />
                <button className="bg-slate-300 px-4 py-2 rounded-sm">Search</button>
            </div>
        </section>
    </article>
}