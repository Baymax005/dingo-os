# ⛓️ Blockchain Guide

Complete guide to blockchain development on Dingo OS.

---

## Overview

Dingo OS provides safe blockchain tools for:

| Category | Tools |
|----------|-------|
| Development | Hardhat, Foundry, Truffle |
| Testing | Ganache, Local testnets |
| Wallets | MetaMask, hardware wallet support |
| Nodes | Ethereum, Bitcoin node installers |
| Monitoring | Block explorers, dashboards |

---

## Development Environment

### Hardhat

```bash
# Create new Hardhat project
mkdir my-project && cd my-project
npx hardhat init

# Compile contracts
npx hardhat compile

# Run tests
npx hardhat test

# Start local network
npx hardhat node
```

### Foundry

```bash
# Create new Foundry project
forge init my-project
cd my-project

# Build
forge build

# Test
forge test

# Deploy
forge create --rpc-url http://localhost:8545 src/MyContract.sol:MyContract
```

### Truffle (Legacy)

```bash
# Create project
truffle init

# Compile
truffle compile

# Migrate
truffle migrate --network development
```

---

## Local Development Networks

### Start Local Testnet

```bash
# Using Dingo CLI
dingo blockchain testnet start

# Options:
dingo blockchain testnet start --port 8545
dingo blockchain testnet start --accounts 20
dingo blockchain testnet start --balance 1000
```

### Hardhat Network

```bash
# Start Hardhat node
npx hardhat node

# Default:
# RPC: http://localhost:8545
# Chain ID: 31337
```

### Ganache

```bash
# GUI version
ganache

# CLI version
ganache-cli

# Options
ganache-cli --port 8545 --accounts 10
```

### Anvil (Foundry)

```bash
# Start Anvil
anvil

# With options
anvil --port 8545 --accounts 10 --balance 10000
```

---

## Wallet Management

### MetaMask

MetaMask browser extension is pre-installed in Firefox/Chrome.

```bash
# Configure local network
Network Name: Dingo Local
RPC URL: http://localhost:8545
Chain ID: 31337
Currency: ETH
```

### Hardware Wallets

```bash
# Ledger support
dingo blockchain wallets setup ledger

# Trezor support
dingo blockchain wallets setup trezor
```

### Wallet Tools

```bash
# Generate wallet
dingo blockchain wallet generate

# Import wallet
dingo blockchain wallet import

# Check balance
dingo blockchain wallet balance 0x...
```

---

## Node Management

### Ethereum Node

```bash
# Install Geth
dingo blockchain node install ethereum

# Start node
dingo blockchain node start ethereum

# Configuration options:
# --network mainnet|sepolia|holesky
# --syncmode snap|full|archive
```

### Bitcoin Node

```bash
# Install Bitcoin Core
dingo blockchain node install bitcoin

# Start node
dingo blockchain node start bitcoin

# Configuration
# ~/.bitcoin/bitcoin.conf
```

### Node Status

```bash
# Check all nodes
dingo blockchain node status

# Check specific node
dingo blockchain node status ethereum

# View logs
dingo blockchain node logs ethereum
```

---

## Smart Contract Development

### Project Structure

```
my-project/
├── contracts/          # Solidity contracts
├── scripts/            # Deployment scripts
├── test/               # Test files
├── hardhat.config.js   # Configuration
└── .env               # Environment variables
```

### Example Contract

```solidity
// contracts/MyToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("MyToken", "MTK") {
        _mint(msg.sender, initialSupply);
    }
}
```

### Compile

```bash
npx hardhat compile
```

### Test

```javascript
// test/MyToken.test.js
const { expect } = require("chai");

describe("MyToken", function () {
  it("Should assign total supply to owner", async function () {
    const [owner] = await ethers.getSigners();
    const Token = await ethers.getContractFactory("MyToken");
    const token = await Token.deploy(1000000);
    
    expect(await token.totalSupply()).to.equal(1000000);
    expect(await token.balanceOf(owner.address)).to.equal(1000000);
  });
});
```

### Deploy

```javascript
// scripts/deploy.js
async function main() {
  const Token = await ethers.getContractFactory("MyToken");
  const token = await Token.deploy(1000000);
  console.log("Token deployed to:", token.address);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
```

```bash
# Deploy to local network
npx hardhat run scripts/deploy.js --network localhost

# Deploy to testnet
npx hardhat run scripts/deploy.js --network sepolia
```

---

## Network Configuration

### Testnets

| Network | Chain ID | Faucet |
|---------|----------|--------|
| Sepolia | 11155111 | [sepolia-faucet.pk910.de](https://sepolia-faucet.pk910.de) |
| Holesky | 17000 | [holesky-faucet.pk910.de](https://holesky-faucet.pk910.de) |
| Goerli | 5 | Deprecated |

### Configure Networks

```javascript
// hardhat.config.js
module.exports = {
  networks: {
    localhost: {
      url: "http://127.0.0.1:8545"
    },
    sepolia: {
      url: `https://sepolia.infura.io/v3/${INFURA_KEY}`,
      accounts: [PRIVATE_KEY]
    }
  }
};
```

---

## Monitoring & Analytics

### Block Explorer

```bash
# Start local block explorer
dingo blockchain explorer start

# Access at http://localhost:4000
```

### Transaction Monitoring

```bash
# Watch pending transactions
dingo blockchain watch pending

# Monitor specific address
dingo blockchain watch 0x...
```

### Dashboard

```bash
# Launch blockchain dashboard
dingo blockchain dashboard

# Shows:
# - Network status
# - Node sync status
# - Recent transactions
# - Gas prices
```

---

## Security Best Practices

### Secure Development

1. **Never commit private keys**
```bash
# Use environment variables
PRIVATE_KEY=xxx npx hardhat run scripts/deploy.js

# Or .env file (gitignored)
echo ".env" >> .gitignore
```

2. **Audit contracts**
```bash
# Run Slither (static analyzer)
slither .

# Run Mythril
myth analyze contracts/MyContract.sol
```

3. **Test thoroughly**
```bash
# Run coverage
npx hardhat coverage
```

### Wallet Security

```bash
# Generate secure wallet
dingo blockchain wallet generate --secure

# Store seed phrase safely
# NEVER share private keys
```

---

## DeFi Tools

### Uniswap Fork

```bash
# Deploy local Uniswap V2 fork
dingo blockchain defi uniswap-v2

# Deploy local Uniswap V3 fork
dingo blockchain defi uniswap-v3
```

### Price Feeds

```bash
# Mock Chainlink price feeds
dingo blockchain defi price-feeds start
```

---

## Troubleshooting

### Common Issues

**Transaction stuck:**
```bash
# Increase gas price
# Cancel with same nonce
npx hardhat run scripts/cancel.js
```

**Node sync issues:**
```bash
# Check sync status
dingo blockchain node status ethereum

# Resync
dingo blockchain node resync ethereum
```

**Contract verification failed:**
```bash
# Ensure source matches deployed bytecode
npx hardhat verify --network sepolia DEPLOYED_ADDRESS
```

### Reset Development Environment

```bash
# Reset local chain
dingo blockchain testnet reset

# Clear cache
rm -rf cache artifacts
npx hardhat clean
```

---

## Resources

- [Solidity Docs](https://docs.soliditylang.org/)
- [Hardhat Docs](https://hardhat.org/docs)
- [Foundry Book](https://book.getfoundry.sh/)
- [OpenZeppelin](https://docs.openzeppelin.com/)
- [Ethereum.org](https://ethereum.org/developers)

---

*Need help? Run `dingo blockchain help` or check our FAQ*
