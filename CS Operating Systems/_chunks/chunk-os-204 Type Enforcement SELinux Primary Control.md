---
id: chunk-csos-204
type: chunk
source: "[[raw-os-039]]"
source_loc: "SELinux and Mandatory Access Control"
topic: "security"
claim: "Type Enforcement is SELinux primary mechanism: deny-by-default rules specify which source process types can perform which operations on which target resource types"
confidence: verified
supports:
  - "[[Access Control]]"
tags:
  - csos
  - csos/security
  - chunk
up: "[[CS Operating Systems]]"
---
# Security — Type Enforcement is SELinux primary access control

## Context

Every process and resource gets a security context (user:role:type:level). Type Enforcement rules follow the form allow source_type target_type : object_class { permissions }. For example, httpd_t can read httpd_sys_content_t files but not user_home_t. Any access not explicitly allowed is denied. SELinux operates in enforcing, permissive, or disabled modes, with targeted policy confining ~200 daemons by default on RHEL/Fedora.

## Why It Matters

Type Enforcement makes SELinux security model concrete. Understanding the allow-rule syntax and deny-by-default principle explains how to write SELinux policy, interpret audit denials (audit2allow), and why even misconfigured services are contained.

## QnA Seeds

- Q: What is the format of a SELinux Type Enforcement allow rule?
- Q: What happens when no allow rule exists for a requested access?
- Q: What does SELinux targeted policy confine by default?
