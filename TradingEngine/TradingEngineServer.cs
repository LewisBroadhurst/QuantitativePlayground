using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Options;

using System;

using TradingEngine.Core.Configuration;

namespace TradingEngine.Core
{
    // inheriting from ITradingEngineServer, which means it must override its methods
    internal class TradingEngineServer : BackgroundService, ITradingEngineServer
    {
        private readonly ILogger<TradingEngineServer> _logger;
        private readonly TradingEngineServerConfiguration _tradingEngineConfiguration;

        public TradingEngineServer(ILogger<TradingEngineServer> logger, IOptions<TradingEngineServerConfiguration> config) 
        {
            _logger = logger ?? throw new ArgumentNullException(nameof(logger));
            _tradingEngineConfiguration = config.Value ?? throw new ArgumentNullException(nameof(config));
        }

        public Task Run(CancellationToken token) => ExecuteAsync(token);

        protected override Task ExecuteAsync(CancellationToken stoppingToken)
        {
            while (!stoppingToken.IsCancellationRequested)
            {

            }
        }
    }
}
