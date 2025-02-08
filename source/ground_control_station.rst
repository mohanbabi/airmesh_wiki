Ground Control Station Setup
============================

There are two major types of Ground Control Stations (GCS) commonly in use:

1. **Mission Planner**
2. **QGroundControl Station**

This guide explains how to connect your Flight Controller to a Ground Control Station over a cellular network for daily operations.

**Power on your Flight Control System**

1. **Join the Tailscale Network:**

   - Ensure your monitoring device (laptop or mobile) is connected to the Tailscale VPN network with a valid data connection.
   - Your Airmesh system and the laptop or mobile device will have separate networks but should be in the same VPN network (Tailscale network).
   - Verify connectivity:
      - Use the `ping` command to check the IP address of the drone. If the ping is successful, you are ready to proceed.
      - If the ping response is not successful, check if:
         - A valid data pack is available.
         - The system is powered on correctly.
   - Open the Ground Control Station software (Mission Planner or QGroundControl Station).

2. **Connect the Ground Control Station to the Flight Controller:**

   - To connect the Ground Control Station (GCS) to the Flight Controller:
      - Enter the **IP address** and **port** in the connection options of the Ground Control Station software.
      - Click on **Connect**. The GCS will start displaying real-time flight data.
   - **Note:** Ensure the IP and port match the settings of your Airmesh system.
   - Refer to the reference video below for detailed instructions.

3. **Test Flight:**

   - Conduct a test flight to ensure proper connectivity and control.
   - Verify telemetry and commands are functioning as expected.

**Reference Video:**

.. youtube:: jVLxVc30e1U
   :width: 100%

========

**Congratulations!**  

Your Airmesh system is now ready for operation.


**Thank You!**

..  raw:: html
    
    <p style="text-align:center;color:green;"><strong>
     We sincerely appreciate your trust in our technology and our unwavering commitment to serving you with loyalty and dedication. Should you encounter any issues or require assistance, please don’t hesitate to reach out.</strong>
    <br></br>
    </p>


Our mission is to educate your team, **increase your operational speed by 50x, and cut costs to half of what you are currently spending with our efficient workflows.** We are here to support you every step of the way and help you achieve unparalleled success.

