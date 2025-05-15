<p align="center">
    <img src="https://img.icons8.com/?size=512&id=55494&format=png" align="center" width="30%">
</p>
<p align="center"><h1 align="center">JSPRINTS</h1></p>
<p align="center">
	<em>Print your moments, elevate your space.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/JCampy/JsPrints?style=plastic&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/JCampy/JsPrints?style=flat-square&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/JCampy/JsPrints?style=flat-square&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/JCampy/JsPrints?style=flat-square&color=0080ff" alt="repo-language-count">
</p>
<p align="center">Built with the tools and technologies:</p>
<p align="center">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat-square&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/CSS-1572B6?logo=css3&logoColor=fff" alt="CSS">
	<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat-square&logo=JavaScript&logoColor=black" alt="JavaScript" />
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Flask-000?logo=flask&logoColor=fff" alt="Flask">
</p>
<br>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

JsPrints is a dynamic open-source project designed to streamline the process of managing and showcasing prints in an e-commerce platform. It simplifies user authentication, product display, and account management, enhancing the overall shopping experience. Ideal for artists and online businesses seeking an efficient and user-friendly platform for selling and purchasing prints.

---

## 👾 Features

|     |      Feature      | Summary                                                                                                                                                                                                                 |
| :-- | :---------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Utilizes **Flask** framework for web application development.</li><li>Follows **MVC** design pattern for separation of concerns.</li><li>Employs **Flask blueprints** for efficient route management.</li></ul> |
| 🔩  | **Code Quality**  | <ul><li>Consistent code formatting and style across the codebase.</li><li>Uses **PEP 8** guidelines for Python code.</li><li>Includes detailed comments and docstrings for better code understanding.</li></ul>         |
| 📄  | **Documentation** | <ul><li>Comprehensive **HTML** documentation with 10 files.</li><li>Includes **requirements.txt** for managing dependencies.</li><li>Provides **.env.example** for defining environment variables.</li></ul>            |
| 🔌  | **Integrations**  | <ul><li>Integrates with **pip** for package management.</li><li>Utilizes **Flask** extensions for additional functionality.</li><li>Supports **HTML** for frontend integration.</li></ul>                               |
| 🧩  |  **Modularity**   | <ul><li>Organized codebase with separate modules for different functionalities.</li><li>Uses **Flask blueprints** for modular route handling.</li><li>Encourages reusable components and functions.</li></ul>           |
| 🧪  |    **Testing**    | <ul><li>Includes testing commands for ensuring code reliability.</li><li>Supports **unit testing** for individual components.</li><li>Provides a structured approach to testing code changes.</li></ul>                 |
| ⚡️ |  **Performance**  | <ul><li>Optimizes code for **fast response times**.</li><li>Utilizes **Flask caching** for improved performance.</li><li>Efficiently handles **HTTP requests** for enhanced user experience.</li></ul>                  |
| 🛡️  |   **Security**    | <ul><li>Implements **secure user authentication** and authorization.</li><li>Protects sensitive data using **environment variables**.</li><li>Ensures **secure file handling** for user uploads.</li></ul>              |
| 📦  | **Dependencies**  | <ul><li>Manages dependencies using **requirements.txt**.</li><li>Specifies exact versions of packages for consistency.</li><li>Ensures compatibility across the codebase architecture.</li></ul>                        |

---

## 📁 Project Structure

```sh
└── JsPrints/
    ├── ecommerce
    │   ├── .env.example
    │   ├── __init__.py
    │   ├── authentication.py
    │   ├── db_models.py
    │   ├── requirements.txt
    │   ├── routes.py
    │   ├── static
    │   └── templates
    └── main.py
```

### 📂 Project Index

<details open>
	<summary><b><code>JSPRINTS/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/JCampy/JsPrints/blob/master/main.py'>main.py</a></b></td>
				<td>Initialize Flask app for ecommerce project, enabling it to run in debug mode.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- ecommerce Submodule -->
		<summary><b>ecommerce</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/JCampy/JsPrints/blob/master/ecommerce/authentication.py'>authentication.py</a></b></td>
				<td>- Handles user authentication and authorization for the e-commerce platform<br>- The code in this file allows users to log in, sign up, and log out securely<br>- It interacts with the database to validate user credentials and create new user accounts, providing a seamless user experience for accessing the platform's features.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/JCampy/JsPrints/blob/master/ecommerce/requirements.txt'>requirements.txt</a></b></td>
				<td>- Manage project dependencies using the provided requirements.txt file to ensure the correct versions of libraries are installed<br>- This file specifies the exact versions of packages required for the ecommerce project, maintaining consistency and compatibility across the codebase architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/JCampy/JsPrints/blob/master/ecommerce/routes.py'>routes.py</a></b></td>
				<td>- SUMMARY:
The `routes.py` file in the `ecommerce` module defines routes and handlers for the web application, including displaying the index page and product pages<br>- It utilizes Flask blueprints to organize and manage the routes efficiently<br>- The file also includes functions for file integrity checking and handling file uploads<br>- This code plays a crucial role in defining the user-facing interactions and content delivery within the e-commerce application.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/JCampy/JsPrints/blob/master/ecommerce/.env.example'>.env.example</a></b></td>
				<td>Defines environment variables for the project, including the secret key and database URI.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/JCampy/JsPrints/blob/master/ecommerce/db_models.py'>db_models.py</a></b></td>
				<td>- Defines database models for an e-commerce platform, including user details, product information, shopping cart, orders, shipping, payments, and purchase history<br>- Establishes relationships between different entities to manage user interactions and transactions effectively within the application.</td>
			</tr>
			</table>
			<details>
				<summary><b>templates</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/JCampy/JsPrints/blob/master/ecommerce/templates/shoppingCart.html'>shoppingCart.html</a></b></td>
						<td>- Generates the shopping cart interface for the ecommerce platform, allowing users to view and manage items in their cart, input personal and payment details, and proceed to checkout<br>- Displays order confirmation upon completion, enhancing the overall shopping experience and facilitating seamless transactions.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/JCampy/JsPrints/blob/master/ecommerce/templates/productDisplay.html'>productDisplay.html</a></b></td>
						<td>- Renders product details and allows adding items to the shopping cart in the ecommerce platform<br>- Displays product information, including name, image, owner, location, and description<br>- Enables users to interact with the product by adding it to the cart for purchase.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/JCampy/JsPrints/blob/master/ecommerce/templates/addProduct.html'>addProduct.html</a></b></td>
						<td>- Enables users to add new products to the ecommerce platform by providing a form with fields for product details, such as name, price, category, and description<br>- Allows users to upload an image of the product<br>- This functionality enhances the platform's capability to expand its product offerings and improve the overall shopping experience for customers.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/JCampy/JsPrints/blob/master/ecommerce/templates/accountManagement.html'>accountManagement.html</a></b></td>
						<td>- Enables users to manage their account details, including updating username, password, email, and addresses<br>- Provides options to update shipping and billing addresses<br>- Includes a feature to sell products<br>- Supports user authentication for personalized account management<br>- Enhances user experience by offering a seamless account management interface within the ecommerce platform.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/JCampy/JsPrints/blob/master/ecommerce/templates/login.html'>login.html</a></b></td>
						<td>- Implements a login form in the ecommerce project, allowing users to input their credentials for authentication<br>- The form includes fields for username/email and password, with options for password recovery and account creation<br>- This file enhances user experience by providing a structured interface for logging into the platform.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/JCampy/JsPrints/blob/master/ecommerce/templates/index.html'>index.html</a></b></td>
						<td>- Render a welcoming homepage for J's Prints, showcasing a range of high-quality prints<br>- The page highlights the brand's dedication to preserving special moments and offers a seamless shopping experience<br>- The layout includes a prominent welcome message, engaging text, and convenient navigation links for contacting the team or browsing products.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/JCampy/JsPrints/blob/master/ecommerce/templates/base.html'>base.html</a></b></td>
						<td>- Defines the base layout for the ecommerce website, including header, navigation, flash messages, and footer sections<br>- Integrates Bootstrap for styling and responsiveness<br>- Manages user authentication, search functionality, and shopping cart display<br>- Supports account management and logout features<br>- Overall, it establishes the foundation for a user-friendly and visually appealing online shopping experience.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/JCampy/JsPrints/blob/master/ecommerce/templates/signup.html'>signup.html</a></b></td>
						<td>- Generates a user signup form for creating an account<br>- The form includes fields for first name, last name, username, email, phone number (optional), and password<br>- Upon submission, the form triggers account creation<br>- Additionally, it provides a link for existing users to sign in.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/JCampy/JsPrints/blob/master/ecommerce/templates/logout.html'>logout.html</a></b></td>
						<td>- Enables users to log out securely from the ecommerce platform<br>- The code in this file provides a seamless and user-friendly experience for customers to safely end their session<br>- This functionality is crucial for maintaining the security and privacy of user accounts within the overall architecture of the project.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/JCampy/JsPrints/blob/master/ecommerce/templates/products.html'>products.html</a></b></td>
						<td>- Generates the product showcase page for an e-commerce platform<br>- Displays products by category, allowing users to view and purchase prints<br>- Includes options for users to sell their own prints if authenticated<br>- Supports navigation to different product categories and individual product details<br>- Enhances user experience by showcasing a variety of products in an organized manner.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with JsPrints, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python 3.10+, HTML, CSS
- **Package Manager:** Pip

### ⚙️ Installation

Install JsPrints using one of the following methods:

**Build from source:**

1. Clone the JsPrints repository:

```sh
❯ git clone https://github.com/JCampy/JsPrints
```

2. Navigate to the project directory:

```sh
❯ cd JsPrints
```

3. Install the project dependencies:

**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />]()

```sh
❯ pip install -r requirements.txt
```

### 🤖 Usage

Run JsPrints using the following command:
**Using**

```sh
❯ python main.py
```

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/JCampy/JsPrints/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/JCampy/JsPrints/issues)**: Submit bugs found or log feature requests for the `JsPrints` project.
- **💡 [Submit Pull Requests](https://github.com/JCampy/JsPrints/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/JCampy/JsPrints
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/JCampy/JsPrints/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=JCampy/JsPrints">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the MIT License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/mit/) file.
