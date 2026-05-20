# Richard Samela | Mobile & Backend Engineer

Product-minded engineer specializing in mobile architecture, data pipelines, and AI integrations.

<div align="center">
  <a href="https://github.com/feromakovi"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Badge" /></a>
  <a href="mailto:feromakovi@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email Badge" /></a>
  <a href="https://feromakovi.github.io/richard_samela_cv.pdf"><img src="https://img.shields.io/badge/Download%20PDF-0077B5?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white" alt="Download PDF Badge" /></a>
</div>

---

## Professional Summary

Senior engineer shipping multimodule Android SDKs and Go BFF plugins across regulated medical, OTT streaming, aviation, and government identity domains. Track record of designing the "sensors and pipelines" — modular client SDKs, telemetry capture, and server-driven UI compositors — that feed downstream intelligence. Handson with LLM agents and on premises model deployment (Gemma, LangChain, MCP, RAG, local Ollama). Startup enthusiast minded and comfortable owning the surface from device sensor to backend contract.

## Core Competencies

- **Languages:** Kotlin, Java, Go, Swift, Bash
- **Mobile & SDK:** Multimodule Gradle (KTS + Groovy), Jetpack Compose, Hilt/Dagger, Coroutines/Flow, Room, Apollo GraphQL, Navigation, Paparazzi, KSP
- **Data & Telemetry:** Bitdrift, Firebase Crashlytics/Performance, WorkManager, Realm, REST/GraphQL ingestion
- **Backend:** Go HashiCorp plugins, Protobuf / OpenAPI, BFF and Server Driven UI
- **Platform & IaC:** Terraform + LaunchDarkly, JFrog Artifactory, custom Gradle plugins
- **CI/CD:** GitHub Actions, GitLab CI, Azure Pipelines, Fastlane, Gradle Enterprise
- **AI:** LangChain (Anthropic / OpenAI / Google / Ollama), MCP, on premises LLM deployment, fine-tuning, agentic CLI tools

## Technical Experience & Highlighted Projects

### Paramount — OTT Mobile & Living-Room Platform
**Role:** Senior Mobile Engineer — contributor inside a large multiteam monorepo.
**Stack:** Kotlin, Jetpack Compose, Hilt, KSP, Coroutines, Bitdrift, Firebase, custom Gradle plugins, Fastlane, GitHub Actions, Gradle Enterprise, Go (BFF), Protobuf/OpenAPI, Terraform + LaunchDarkly.

- Built lightweight, versioned client SDKs (identity, payments, storage, logging, persistence) with clean public API surfaces consumed by both mobile and TV clients.
- Integrated high frequency telemetry capture and Firebase observability — enabling realtime ingestion of user state signals.
- Contributed Go plugins to the page/widget BFF compositor — server-driven UI rendering against strict, typed data contracts.
- Managed feature flag activations via Terraform (defined LaunchDarkly configuration) — decoupling release cadence from client deployments.

### Roche — Regulated Medical Device Ecosystem
**Role:** Module contributor inside a regulated multiproduct monorepo.
**Stack:** Kotlin, Compose (interop migration), Dagger/Hilt, BLE, JFrog Artifactory, Paparazzi screenshot testing, pitest mutation testing, Dokka, Compose design tokens synced from Figma.

- Shipped versioned, isolated SDK artifacts respecting strict cross-module isolation rules under a regulated software workflow — safe consumption by multiple host applications.
- Contributed to BLE driven CGM and insulin pump telemetry layers — reliable, low latency device data feeding the consumer companion application.
- Advanced a Compose based design system with Figma token sync and Paparazzi snapshot coverage — consistent UI surface across regulated apps and faster designer/engineer iteration.

### Disney — OTT Streaming SDK Suite & TV App
**Role:** SDK and application engineer.
**Stack:** Kotlin, Jetpack Compose, Hilt, ExoPlayer + IMA, Mux analytics, Apollo / REST, JFrog Artifactory, custom Gradle plugins, Azure Pipelines, Fastlane, Terraform + LaunchDarkly.

- Built distributable Android SDKs (player, ads rendering, network, data layer, feature gating) published via Artifactory — lightweight footprints consumed by mobile, TV, and Fire TV applications.
- Integrated ads, player analytics, and live ads pipelines — unified instrumentation across consumer surfaces.
- Maintained Terraform for staged and production environments — GitOps driven feature rollouts.

### Embedded Payment Systems — POS & Vending Terminals
**Role:** Android / Hardware Integration Engineer
**Stack:** Android, Kotlin, NFC, APDU Commands, MDB Protocol, Hardware Peripherals

- **Android POS Terminal:** Engineered the payment communication layer for an Android based point of sale (POS) device. Interfaced directly with hardware peripherals and implemented NFC communication using APDU commands to read payment card data and drive secure transaction operations.
- **Vending Machine Retrofit:** Developed an end-to-end terminal application to upgrade legacy, cash-only vending machines. Integrated the MDB protocol to bridge the embedded hardware with modern payment networks, enabling contactless, QR code, and SDK-driven card payments.

### RSys / NWS — Aviation Tracking & Document-Capture Pipelines
**Role:** Lead Android engineer; iOS parity contributor.
**Stack:** Kotlin, Jetpack Compose, Hilt, Coroutines, Realm, Apollo GraphQL, OpenCV, Firebase, Fastlane, GitLab CI; Swift, Apollo iOS, Tuist, CocoaPods on the iOS side.

- Implemented offline first sensor, map, and flight plan data flow for a general aviation flight tracking app — resilient operation in low connectivity airborne scenarios.
- Built a camera → crop → GraphQL upload document capture pipeline — high fidelity data ingestion into a typed backend schema.
- Mirrored data contracts across Android and iOS clients — contract parity and reduced backend integration risk.

### Slovak eID / Autogram — Government Identity & Qualified Electronic Signing
**Role:** SDK and multiplatform engineer.
**Stack:** Kotlin, Koin, Retrofit, Coroutines on the native SDK side; Flutter, Chopper, Firebase on the multiplatform application side; NFC, eIDAS qualified signing.

- Integrated NFC ID card authentication and qualified electronic signing — eIDAS compliant identity flows on mobile.
- Bridged a native Android eID SDK into a Flutter application — multiplatform reach without sacrificing native grade security.

## AI & Product Initiatives

- **On premise LLM for a client (accounting firm).** Deployed Gemma locally on client premises for confidential document. Owned the full setup — model retrieval, runtime environment, and surrounding ecosystem — under strict confidentiality requirements driven by the client's sensitive accounting data. Experimented with fine-tuning on client documents to better match domain language.
- **Autonomous LangChain based research agent.** Multi-provider (Anthropic, OpenAI, Google, Ollama) with LangSmith evaluations, a planner/scratchpad loop, browser tooling, and a pluggable "Skills" extension model.
- **Agentic mobile development.** Drove multiplatform native parity (iOS / Android / Web) using agent assisted workflows.
- **Continuous tracking** of the AI tooling ecosystem — LangChain, MCP, RAG patterns, local LLMs (Ollama), and model deployment tradeoffs — directly transferable to AI pipelines that turn noisy data into structured, actionable intelligence.
