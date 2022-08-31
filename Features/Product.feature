Feature: Test the Amazon Application
    Scenario: Verify adding Products
      Given Amazon is launched in Chrome
      When We Select product Category
      Then We fetch product Details
      And We Validate details of Product1
