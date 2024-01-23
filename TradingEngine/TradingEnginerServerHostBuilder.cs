using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using TradingEngine.Core.Configuration;

namespace TradingEngine.Core
{
    public sealed class TradingEnginerServerHostBuilder
    {
        public static IHost BuildTradingEnginerServer()
            => Host.CreateDefaultBuilder().ConfigureServices((context, services) =>
            {
                // context allows us to index into our configuration

                // Starting with configuration...
                services.AddOptions();
                services.Configure<TradingEngineServerConfiguration>(context.Configuration.GetSection(nameof(TradingEngineServerConfiguration)));


            }).Build();

    }
}
