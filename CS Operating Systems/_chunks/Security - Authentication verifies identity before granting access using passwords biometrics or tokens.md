---
id: chunk-csos-045
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 9"
topic: "security"
claim: "Authentication verifies identity before granting access using knowledge factors (passwords), possession factors (tokens), or inherence factors (biometrics); multi-factor combines two or more categories"
confidence: verified
supports:
  - "[[Authentication and Protection]]"
tags:
  - csos
  - csos/security
  - chunk
up: "[[CS Operating Systems]]"
---
# Security — Authentication verifies identity before granting access using passwords biometrics or tokens

## Context

Passwords are the most common authentication factor but are easily compromised (reuse, weak choices, phishing, database breaches). Secure storage requires salted slow hashing (bcrypt, scrypt, Argon2) — not MD5 or SHA-1 which can be reversed via rainbow tables. Possession factors (hardware security keys like YubiKey, TOTP apps) require the attacker to physically possess the device. Biometrics (fingerprint, face) are convenient but cannot be revoked if compromised. MFA combines two or more factor types, raising the attack cost significantly.

## Why It Matters

Authentication is the gate between the public internet and protected resources. Every major breach either bypassed authentication entirely (via an unauthenticated vulnerability) or compromised credentials (phishing, credential stuffing). Understanding the security properties of each authentication factor — and why MFA is necessary for high-value accounts — is a core OS and security engineering concept.

## QnA Seeds

- Q: What is the difference between a hash function and a slow password hash like bcrypt?
- Q: Why can't biometrics be "revoked" if compromised?
- Q: What authentication protocol does Windows Active Directory use and how does it work?
