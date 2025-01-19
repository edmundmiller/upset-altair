## [0.2.0] (2025-01-18)

### Changed

- Updated to support Altair 5.0.0 and Vega-Lite 5
- Replaced `alt.selection_multi()` with `alt.selection_point()` for legend selection
- Removed width/height properties from VConcatChart level
- Set width/height properties on individual chart components for proper validation
- Updated PNG snapshot generation to use Altair's built-in saving capabilities

### Added

- Comprehensive documentation in `docs.md`
- Detailed API reference with parameter descriptions
- Interactive features documentation
- Usage examples in documentation

### Fixed

- Fixed deprecation warning for selection_multi
- Fixed PNG snapshot generation and tracking
- Resolved validation errors for chart sizing in Altair 5

## [0.1.1] - Split into separate package (2025-01-18)

- Split the original function into a separate files for devision of concerns

## [0.1.0] - Initial Release (2025-01-18)

### Added

- Initial implementation of UpSetAltair
- Basic set visualization functionality
- Interactive features (hover highlighting, legend filtering)
- Support for customization (colors, sizes, sorting)
