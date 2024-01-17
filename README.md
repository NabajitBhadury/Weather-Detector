# Weather Detector Documentation

<div align="center">
<img src="https://t4.ftcdn.net/jpg/04/85/17/33/360_F_485173339_rHVWOWEwZneJpHqgFNiYJLSPQg7hNoAA.jpg" width="60%"></div>

### Introduction
Welcome to the Weather Detector project! This web application is built using Django, HTML, CSS, and JavaScript to provide users with real-time weather information for any city around the world.

### Features
*City Search:* Users can search for the weather of any city by entering its name in the search bar.

*Real-time Weather Data*: The app fetches real-time weather data using a third-party API, ensuring that users get the latest and most accurate information.

*Responsive Design*: The application is designed to be responsive, providing a seamless experience across various devices, including desktops, tablets, and smartphones.

### Installation
To run the Weather App locally, follow these steps:

### Clone the Repository:

```
git clone https://github.com/your-username/weather-app.git
```

### Navigate to the Project Directory:

```
cd weather-app
```

### Install Dependencies:

```
pip install django
```

### Configure API Key:
Obtain a free API key from a weather data provider (e.g., OpenWeatherMap).
Copy the API key to the settings.py file in the weather app.

### Run Migrations:

```
python manage.py migrate
```

### Run the Development Server:

```
python manage.py runserver
```

### Visit the Application:

Open your web browser and go to *http://127.0.0.1:8000/*  to access the Weather App.

### Configuration

### API Key:
Obtain a free API key from a weather data provider (e.g., OpenWeatherMap).
Update the WEATHER_API_KEY variable in the settings.py file with your API key.
### Technologies Used
*Django:* The web framework used for the backend development.
*HTML, CSS, JavaScript:* Frontend technologies for creating an interactive user interface.
*Third-party Weather API:* Used to fetch real-time weather data.


## Contribution 🚀

We welcome contributions from the community! If you'd like to contribute to this project, follow these steps:

1. **Fork the Repository:**
   - Click on the "Fork" button at the top right corner of the repository page.

2. **Clone Your Fork:**
   - Clone the repository from your GitHub account to your local machine.
     ```bash
     git clone https://github.com/your-username/Weather-Detector.git
     ```

3. **Create a Branch:**
   - Create a new branch for your contribution.
     ```bash
     git checkout -b feature-branch
     ```

4. **Make Changes:**
   - Make your desired changes to the HTML and CSS files.

5. **Commit Changes:**
   - Commit your changes with a descriptive commit message.
     ```bash
     git commit -m "Add feature or fix"
     ```

6. **Push Changes:**
   - Push your changes to your fork on GitHub.
     ```bash
     git push origin feature-branch
     ```

7. **Create a Pull Request:**
   - Open a Pull Request (PR) on the original repository.
   - Provide a clear title and description for your PR.

8. **Review and Merge:**
   - The maintainers will review your PR and may request changes.
   - Once approved, your changes will be merged into the main branch.

## Syncing with Upstream 🔄

If the original repository has been updated, sync your fork to include the latest changes:

1. **Add Upstream Remote:**
   - Add the upstream repository as a remote.
     ```bash
     git remote add upstream https://github.com/original-username/Weather-Detector.git
     ```

2. **Fetch Upstream Changes:**
   - Fetch the changes from the upstream repository.
     ```bash
     git fetch upstream
     ```

3. **Merge Upstream Changes:**
   - Merge the changes from the upstream repository into your local branch.
     ```bash
     git merge upstream/main
     ```

4. **Push Changes to Your Fork:**
   - Push the updated changes to your fork on GitHub.
     ```bash
     git push origin main
     ```

## Rollback a Commit ⏪

If you need to undo a commit, you can use the following command:

```bash
git revert <commit-hash>
```
Replace <commit-hash> with the actual hash of the commit you want to revert.


## Contributors ✨

Thanks goes to these wonderful people 💜
<table>
  <tr>
    <td align="center"><a href="https://github.com/NabajitBhadury"><img src="https://avatars.githubusercontent.com/u/117065551?v=4" width="100px;" alt=""/><br /><sub><b>Nabajit Bhadury</b></sub></a><br /><a href="#maintenance-Tlazypanda" title="Maintenance">🚧✍️🖥️</a></td>
    <td align="center"><a href="https://github.com/bluecoder2003"><img src="https://avatars.githubusercontent.com/u/130232862?v=4" width="100px;" alt=""/><br /><sub><b>bluecoder2003</b></sub></a><br /><a title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/abhipriyachowdhury"><img src="https://avatars.githubusercontent.com/u/139592613?v=4" width="100px;" alt=""/><br /><sub><b>Abhipriya Chowdhury</b></sub></a><br /><a  title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/RichPerspective007"><img src="https://avatars.githubusercontent.com/u/121783925?v=4" width="100px;" alt=""/><br /><sub><b>SHIVADITYA BHATTACHARYA</b></sub></a><br /> <a  title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/AnuragMalasi"><img src="https://avatars.githubusercontent.com/u/125523667?v=4" width="100px;" alt=""/><br /><sub><b>Anurag4002</b></sub></a><br /><a  title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/arghadipmanna101"><img src="https://avatars.githubusercontent.com/u/130065095?v=4" width="100px;" alt=""/><br /><sub><b>Arghadip Manna</b></sub></a><br /><a title="Code">💻</a></td>

  </tr>
  </table>

### License
This project is licensed under the [MIT License](https://chat.openai.com/c/LICENSE.md).

<div align="center">
<img src="https://media.giphy.com/media/8xJHqEUg4SNJhJBHzn/giphy.gif" width="30%"></div>

Thank you for using the Weather App! Stay informed about the weather in any city around the world.
