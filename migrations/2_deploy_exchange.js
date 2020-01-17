const exchange = artifacts.require('./uniswap_exchange');

module.exports = function(deployer, network, accounts) {
  deployer.deploy(exchange, accounts[0]);
};
