const factory = artifacts.require('./uniswap_factory');
const exchange = artifacts.require('./uniswap_exchange');

module.exports = function(deployer) {
  deployer
      .then(() => factory.deployed())
      .then(contract => contract.initializeFactory(exchange.address));
};
