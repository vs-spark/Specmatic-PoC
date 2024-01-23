Feature: Employees API

  Background:
    Given openapi ./employees-without-examples.yaml

  Scenario Outline: Create Employee
    When POST /znsio/specmatic/employees
    Then status 201
    Examples:
      | id | name     | department  | designation |
      | 70 | Jill Doe | Engineering | Director    |

  Scenario Outline: Get Employee Success
    When GET /znsio/specmatic/employees/(id:number)
    Then status 200
    Examples:
      | id | name     | department  | designation         |
      | 10 | Jane Doe | Engineering | Engineering Manager |

  Scenario Outline: Get Employee Not Found Error
    When GET /znsio/specmatic/employees/100
    Then status 404

  Scenario Outline: Update Employee Success
    When PUT /znsio/specmatic/employees/10
    Then status 200
    Examples:
      | id | (REQUEST-BODY)                                                                             |
      | 10 | { "id": 10, "name": "Jill Doe", "department": "Engineering", "designation": "Director" } |
