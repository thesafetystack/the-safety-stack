# Release manifests

One directory per dataset release, named by its date, with byte-for-byte copies of that release's `release.json`
(the manifest: build, row counts, taxonomy versions with sha256, override files, policy, every file with its size and
sha256) and `SHA256SUMS`. They let a reader tell what each release contained without downloading it. The checksums
describe the files on Hugging Face; the copies of FORMAT.md, QUALITY.md, CHANGELOG.md and VOCAB.md in `dataset/`
carry an added header line and so differ from them.

- [2026-10-25](2026-10-25/): the first release.
