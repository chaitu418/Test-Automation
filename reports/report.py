import pytest
import allure

@allure.feature("Feature1")
@allure.story("Story1")
def test_example():
    with allure.step("Step 1: Perform some action"):
        # Your test code here
        pass
