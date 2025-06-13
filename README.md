# Numerical Methods Course

This repository contains implementations of various numerical methods and algorithms for solving mathematical problems. The course covers fundamental numerical analysis techniques and their practical applications.

## Course Structure

### 1. Root Finding Methods
Implementation of various methods for finding roots of non-linear equations:
- Bisection Method
- Newton's Method
- Modified Newton's Method
- Secant Method

Features:
- Root separation algorithm
- Multiple test functions
- Accuracy analysis and convergence comparison
- Interactive command-line interface

### 2. Algebraic Interpolation
Implementation of interpolation methods:
- Newton's Interpolation
- Lagrange Interpolation

Features:
- Support for arbitrary functions
- Error analysis
- Interactive node selection
- Comparison of interpolation methods

### 3. Inverse Interpolation
Implementation of inverse interpolation methods:
- Newton's Inverse Interpolation
- Lagrange Inverse Interpolation

Features:
- Function value to argument mapping
- Error analysis
- Multiple interpolation approaches

### 4. Additional Topics
The course also covers:
- Numerical integration
- Differential equations
- Linear systems
- Matrix operations

## Requirements

- Python 3.x
- C++ compiler (for the root finding module)
- CMake (for building C++ projects)

## Project Structure

```
num_methods/
├── 1/                  # Root finding methods (C++)
│   ├── 1.cpp
│   └── CMakeLists.txt
├── 2/                  # Algebraic interpolation
│   └── main.py
├── 3/                  # Inverse interpolation
│   ├── main.py
│   ├── main_2.py
│   └── main_3.py
├── 4/                  # Additional numerical methods
│   ├── main.py
│   └── test.py
├── 5/                  # More numerical methods
│   ├── main.py
│   └── test.py
└── 6/                  # Advanced numerical methods
    ├── main.py
    └── test.py
```

## Building and Running

### C++ Projects
```bash
cd 1
mkdir build
cd build
cmake ..
make
./1
```

### Python Projects
```bash
cd <project_directory>
python main.py
```

## Features

- Interactive command-line interfaces
- Comprehensive error analysis
- Multiple implementation approaches
- Test cases and validation
- Performance comparisons
- Documentation and comments

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 