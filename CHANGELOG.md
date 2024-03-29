# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security

## [0.0.5] - 2023-03-11

### Added
- Added support for Python 3.11.

### Removed
- Dropped support for Python 3.7.

## [0.0.4] - 2022-10-04

### Changed
- Sped up prediction.

## [0.0.3] - 2022-06-03

### Added
- `LongestStringMatching`: Add basic test
- Added Python 3.10 support.

### Changed
- `LongestStringMatching`: Reduce memory use by not storing words
  of length 1 in training.
- Switched to the top-level `src/` and `tests/` package structure

### Deprecated
### Removed
- Dropped Python 3.6 support.

### Fixed
### Security

## [0.0.2] - 2020-10-11

### Added
- Added support for Python 3.9.

## [0.0.1] - 2020-10-10

First release, starting with two basic models:
`RandomSegmenter` and `LongestStringMatching`.
