Connections Diagram
===================

Airmesh is a plug-and-play device, but maintaining a sufficient and redundant power supply is crucial for optimal performance. Ensure a steady power supply of **5 volts and 2 amps**, which is required by the current telemetry system. Follow the circuit diagrams below to ensure proper power sourcing.

.. tip::
      **Tip**: To view the full diagram in a new tab, hold **Ctrl + Click** (or **Cmd + Click** on macOS) on the image.

1. **Give 5 Volts from Power Module:**
   - Providing 5 volts from two power modules enhances the stability of your autopilot system:
     - **Primary Power Module**: Mandatory for the system’s operation.
     - **Secondary Power Module**: Optional but recommended for redundancy and increased stability.
     - **Connection Details**:
       - Connect the main power to the Power Module.
       - Connect the Power Module to Pixhawk power-port1 and power-port2.
   - **Refer to the circuit diagram below for setup**:

   .. image:: ./images/drawing1.png
      :width: 80%
      :align: center
      :alt: Diagram showing connections for power module setup.

2. **Give 5 Volts from UBEC to Servo Pins of Pixhawk:**
   - Power from UBEC:
     - This power supply comes from a UBEC (Universal Battery Elimination Circuit) with a power rating of **5 volts and 7 amps**.
     - It powers payloads and servos, especially for fixed-wing systems.
   - **Refer to the circuit diagram below for details**:

   .. image:: ./images/drawing.png
      :width: 80%
      :align: center
      :alt: Diagram showing connections for Pixhawk servo power setup.

3. **Connect Airmesh to Telemetry-Port1:**
      - Airmesh has 4 wires:
         - **RED**: (+5V) – Power supply.
         - **BLACK**: (GND) – Ground connection.
         - **WHITE**: (Data) – Connect to the Pixhawk TX pin of the telemetry port.
         - **GREEN**: (Data) – Connect to the Pixhawk RX pin of the telemetry port.

   **Note**:
   Some boards' telemetry ports may not deliver the required power. In such cases, follow the instructions below:
      - If the Wi-Fi does not turn on, it indicates a problem with the power supply. An external power supply is required. Safely unplug the **RED** and **BLACK** wires from the pin housing and connect them to the Pixhawk servo port using a servo pin housing.
      - Ensure that the cables used are of appropriate length and gauge to maintain a secure and reliable connection.
      - For any modifications to extend or adapt the cables, ensure proper insulation to avoid short circuits and prevent overloading the power supply.

   - **Refer to the circuit diagram below for details**:

   .. image:: ./images/drawing.png
      :width: 80%
      :align: center
      :alt: Diagram showing connections for Airmesh telemetry setup.

4. **Important Notes:**
      - Follow these steps to ensure a proper setup:
         - Carefully refer to the circuit diagram provided in the documentation to connect all components accurately.
         - Verify that the system is powered up correctly to avoid any issues.
         - Double-check all connections in your system to ensure they are secure and properly aligned.

   .. image:: ./images/drawing.png
      :width: 80%
      :align: center
      :alt: Diagram showing the overall system connections.
