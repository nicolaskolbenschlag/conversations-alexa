# Integration for Conversation-Tools into Alexa

This repository contains the implementation for an Amazon Alexa Skill that connects to [Voiceflow](https://www.voiceflow.com/). Is is written in Python and supposed to be hosten on AWS Lambda (as suggested in the Alexa Developer Portal).

## Usage

This section shows how to configure the skill.

### Voiceflow

#### Obtaining the voiceflow api-key

1. Open the dialog voiceflow Designer.

2. Navigate to **Integration** and **Dialog API**.

3. Copy the **Primary Key**.

### Setting up the Alexa Skill

1. Login at [Alexa Developer Console](https://developer.amazon.com) (with same account/email-address as alexa account) and click on **Alexa Skills Kit**.

2. Click **Create Skill**.

3. Give it a name and choose your locale. Then click **next**.

4. At *Choose a type of experience*, choose **Games & Trivia**, at *Choose a model* **Custom**, and at *Hosting services* **Alexa-hosted (Python)**, including your preferred *Hosting region*.

5. Choose the *Start from Scratch* template and click **Create Skill**.

6. The tab *Build*:

    > * Change the invocation name (*Invocations > Skill Invocation Name*) to "voiceflow integration", for instance.
    > * Go to *Assets > Slot Types* and click **+ Add Slot Type**. Name it **promptType** and click **Next**. Enter any two or three sentences like "Das ist ein Test." and "Dieser Skill is cool.".
    > * Go to *Interaction Model > Intents* and click **+ Add Intent**. Name it **ResponseIntent** and click **Create custom intent**. At the **Intent Slot**-section, create a slot named **prompt** (click **+**) and choose **promptType** as *Slot Type*. Above, enter **{prompt}** to *Sample Utterances* and click **+**.
    > * Delete the **HelloWorldIntent**.
    > * Click **Save Model**.
    > * Click **Build Model**. Wait until the build is finished.

7. In the tab *Code*, replace the content of the files **lambda_function.py** and **utils.py** with the files in this repository. (Save both file changes by clicking the button **Save**.) Do not forget to replace **\<YOUR-API-KEY-HERE>** in **utils.py** with your voiceflow api-key. Click **Deploy**.

8. In the tab *Test*, select "Development" in **Skill testing is enabled in:**. You can test the skill in this tab.

9. Done! The skill should be available on your Alexa.
