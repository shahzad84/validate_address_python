
```markdown
# Address Validation

This project validates addresses against PIN codes using the India Postal API.

## Usage

The `validate_address` function takes an address and PIN code, calls the API to validate, and returns True if valid:

```python
validate_address(address, pincode)
```

Sample usage:

```python
addresses = [
  "Address 1",
  "Address 2"  
]

pincodes = ["110001", "110002"]

for address, pincode in zip(addresses, pincodes):
  print(validate_address(address, pincode)) 
```

The API response is parsed to check if the address contains any of the post office names returned for that PIN.

## Requirements

- requests
- API key from [India Postal API](https://www.postalpincode.in/Api-Details)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```