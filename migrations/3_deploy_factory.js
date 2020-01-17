const factory = artifacts.require('./uniswap_factory');

module.exports = function(deployer) {
  deployer.deploy(factory);
};
