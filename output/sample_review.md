# AI Code Review Report

**File:** sample.py
**Review Mode:** thorough
**Overall Score:** 65/100

## Summary

Demo review generated with sample findings.

## Findings

### 1. High - Security

**Line:** 3

**Issue:** Hardcoded credentials may expose sensitive information.

**Recommendation:** Use environment variables to store credentials.

### 2. Medium - Code Quality

**Line:** 6

**Issue:** Missing error handling may cause unexpected failures.

**Recommendation:** Add appropriate exception handling.

## Positive Aspects

- Code is relatively simple.
- Function names are understandable.