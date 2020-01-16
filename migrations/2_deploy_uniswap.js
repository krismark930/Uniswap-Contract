var exchange = artifacts.require('./uniswap_exchange');
var factory = artifacts.require('./uniswap_factory');

module.exports = function(deployer, network, accounts) {
  deployer.deploy(exchange, accounts[0]);
  deployer.deploy(factory);
}
