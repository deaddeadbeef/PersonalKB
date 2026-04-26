---
tags: [cs-os, raw]
source_type: textbook_topic
source_title: "SELinux and Mandatory Access Control"
authors: Smalley, Vance, Salamon; NSA
year: 2001
---

# SELinux and Mandatory Access Control

## Summary

SELinux (Security-Enhanced Linux) implements Mandatory Access Control (MAC) in the Linux kernel, supplementing the traditional Discretionary Access Control (DAC) model. Under DAC, file owners control access permissions (chmod, chown), and any process running as a user inherits that user's permissions. This creates a fundamental security weakness: if an application running as a user is compromised, the attacker gains all of that user's access rights. MAC enforces access policies defined by a central administrator that no user or process can override, regardless of ownership or privileges.

SELinux assigns a **security context** (label) to every process (subject) and every resource (file, socket, device). A context consists of three components: user identity, role, and type (e.g., `unconfined_u:unconfined_r:httpd_t`). **Type Enforcement (TE)** is the primary access control mechanism: policy rules specify which source types can perform which operations on which target types. For example, a rule might state that `httpd_t` (the Apache web server type) can read files of type `httpd_sys_content_t` but cannot access files of type `user_home_t`. Any access not explicitly permitted by a rule is denied by default (deny-by-default).

**Role-Based Access Control (RBAC)** in SELinux restricts which types a user can transition to based on their assigned role, limiting the attack surface even if a type enforcement rule exists. **Multi-Level Security (MLS)** adds sensitivity labels (classification levels like Confidential, Secret, Top Secret) and categories, implementing the Bell-LaPadula model ("no read up, no write down") for environments requiring information flow control.

SELinux operates in three modes: `enforcing` (policy actively enforced), `permissive` (policy violations logged but allowed), and `disabled`. Policy can be in `targeted` mode (only specific daemons are confined, everything else runs unconfined) or `strict`/`mls` mode (everything is confined). The `audit2allow` tool converts denial audit logs into policy rules, assisting in policy development.

**AppArmor** is an alternative MAC framework that uses path-based profiles rather than labels, making it simpler to configure but less flexible. AppArmor profiles define which files a program can access by pathname, which capabilities it can use, and which network operations it can perform. Android integrates SELinux to enforce per-app sandboxing: each app runs with a unique type, and policy restricts inter-app access to only explicitly permitted Binder IPC and content provider paths.

## Key Claims

- MAC enforces administrator-defined access policies that no user or process can override, addressing the fundamental DAC weakness where compromised applications inherit all of the user's access rights
- Type Enforcement is SELinux's primary mechanism, using deny-by-default rules that specify allowed operations between source process types and target resource types
- RBAC layers over Type Enforcement to restrict which types a user can assume based on their role, limiting lateral movement even when type rules are permissive
- AppArmor provides a simpler path-based alternative to SELinux's label-based model, trading flexibility and granularity for ease of profile creation and maintenance
- Android's integration of SELinux enforces per-app isolation at the kernel level, with each app running under a unique type that restricts its system access beyond what the Unix DAC model provides

## Atomic Facts

1. A SELinux security context has the form `user:role:type:level`, where type is the most operationally important field for Type Enforcement decisions
2. SELinux policy rules follow the form `allow source_type target_type : object_class { permissions }`, e.g., `allow httpd_t httpd_sys_content_t : file { read open getattr }`
3. The `restorecon` command resets file security contexts to the default values defined by the file contexts policy, commonly needed after moving files or restoring from backup
4. SELinux `targeted` policy on RHEL/Fedora confines approximately 200 daemons by default, while user processes run in the `unconfined_t` domain
5. AppArmor profiles are stored in `/etc/apparmor.d/` as text files named after the program path (e.g., `usr.sbin.apache2`), using `r`, `w`, `x`, `m`, `k` permission flags on file paths
6. Android SELinux policy (since Android 5.0) assigns each app a type like `untrusted_app` or `platform_app`, with Binder IPC permissions controlled by `binder_call` rules between types

## Significance

SELinux represents the most comprehensive implementation of Mandatory Access Control in a mainstream operating system. It shifts the security model from trusting applications to behave correctly (DAC) to enforcing what applications can do regardless of their intent (MAC). Understanding MAC is essential for systems security, compliance with government and military security standards (CC EAL4+), and comprehending how modern mobile operating systems (Android) achieve application sandboxing. The DAC-vs-MAC distinction is a foundational concept in OS security theory.

## Chunks Extracted

*Pending*
