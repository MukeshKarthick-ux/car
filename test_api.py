#!/usr/bin/env python3
"""
Test script for Policy Compliance Checker API
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_health_check():
    """Test the health check endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✅ Health check passed")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

def test_compliance_check(action, expected_result=None):
    """Test compliance checking"""
    try:
        response = requests.post(
            f"{BASE_URL}/check",
            json={"action": action},
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            result = data.get("result", "")
            print(f"📋 Action: {action}")
            print(f"📊 Result: {result}")

            if expected_result and expected_result in result:
                print("✅ Expected result matched")
            elif expected_result:
                print(f"⚠️  Expected '{expected_result}' but got different result")

            print("-" * 50)
            return True
        else:
            print(f"❌ API error: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"❌ Request error: {e}")
        return False

def main():
    print("🧪 Testing Policy Compliance Checker API")
    print("=" * 50)

    # Test health check
    if not test_health_check():
        print("❌ Cannot proceed with tests - API not responding")
        return

    # Test various compliance scenarios
    test_cases = [
        ("I want to work from home tomorrow", "NON-COMPLIANT"),
        ("I need to work overtime this weekend", "COMPLIANT"),
        ("I want to install unauthorized software", "NON-COMPLIANT"),
        ("I want to post company info on social media", "NON-COMPLIANT"),
        ("I need to attend a training session", "COMPLIANT"),
    ]

    passed = 0
    total = len(test_cases)

    for action, expected in test_cases:
        if test_compliance_check(action, expected):
            passed += 1

    print(f"📊 Test Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed!")
    else:
        print("⚠️  Some tests failed - check the output above")

if __name__ == "__main__":
    main()