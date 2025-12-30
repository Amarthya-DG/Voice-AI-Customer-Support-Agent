# 🎙️ Voice AI Hotel Customer Support Agent

A real-time voice AI agent for hotel customer support, powered by **Deepgram's Speech-to-Speech API** and **Twilio**. This agent handles natural phone conversations for hotel reservations, modifications, cancellations, and general inquiries.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Deepgram](https://img.shields.io/badge/Deepgram-Voice_AI-green.svg)
![Twilio](https://img.shields.io/badge/Twilio-WebSockets-red.svg)

## ✨ Features

- **Real-time Voice Conversations** - Natural phone-based interactions with bidirectional audio streaming
- **Interrupt Handling (Barge-in)** - Users can interrupt the AI mid-response for natural conversation flow
- **Function Calling** - AI dynamically executes hotel operations during live conversations
- **Complete Hotel Management** - Lookup, modify, and cancel reservations with policy enforcement

### Supported Operations

| Function | Description |
|----------|-------------|
| `get_hotel_info` | Retrieve hotel amenities, policies, room types, and contact information |
| `lookup_reservation` | Look up existing reservations by confirmation number |
| `cancel_reservation` | Process cancellations with automatic fee calculation based on policy |
| `modify_reservation` | Change dates, room types, guest count, or add special requests |
| `request_callback` | Schedule callbacks for complex issues requiring human agents |

## 🏗️ Architecture

```
┌─────────────┐     WebSocket      ┌─────────────────┐     WebSocket      ┌──────────────┐
│   Twilio    │◄──────────────────►│  Python Server  │◄──────────────────►│   Deepgram   │
│  (Phone)    │   Audio Streaming  │   (main.py)     │   Speech-to-Speech │   Voice AI   │
└─────────────┘                    └────────┬────────┘                    └──────────────┘
                                            │
                                            ▼
                                   ┌─────────────────┐
                                   │ Hotel Functions │
                                   │ (Function Call) │
                                   └─────────────────┘
```

**How it works:**
1. User calls via Twilio → Audio streams to Python server via WebSocket
2. Server forwards audio to Deepgram's Voice Agent API
3. Deepgram transcribes speech, processes with LLM, and returns audio response
4. When the AI needs data (e.g., reservation lookup), it triggers a **function call**
5. Server executes the function and returns results to Deepgram
6. Deepgram incorporates the data into its spoken response

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- [Deepgram API Key](https://console.deepgram.com/)
- [Twilio Account](https://www.twilio.com/) with a phone number
- [ngrok](https://ngrok.com/) (for local development)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/voice-ai-hotel-agent.git
   cd voice-ai-hotel-agent
   ```

2. **Install dependencies**
   ```bash
   pip install websockets python-dotenv
   ```

3. **Set up environment variables**
   ```bash
   # Create .env file
   echo "DEEPGRAM_API_KEY=your_api_key_here" > .env
   ```

4. **Run the server**
   ```bash
   python main.py
   ```

5. **Expose with ngrok** (for Twilio to reach your local server)
   ```bash
   ngrok http 5000
   ```

6. **Configure Twilio**
   - Set your Twilio phone number's webhook to your ngrok URL
   - Configure for WebSocket streaming

## 📁 Project Structure

```
voice-ai-hotel-agent/
├── main.py              # WebSocket server & audio streaming logic
├── hotel_functions.py   # Hotel operations (reservations, policies, etc.)
├── config.json          # Deepgram Voice Agent configuration
├── .env                 # API keys (not tracked in git)
└── README.md
```

## 🔧 Configuration

The `config.json` file configures the Deepgram Voice Agent:

- **Audio Settings**: 8kHz mulaw encoding (Twilio-compatible)
- **Speech Recognition**: Deepgram Nova-3 model
- **LLM**: GPT-4o-mini for conversation handling
- **Text-to-Speech**: Deepgram Aura-2 voice
- **Functions**: Hotel operation definitions for function calling

## 💬 Example Conversation

```
Agent: "Hello! Thank you for calling Grand Horizon Hotel & Spa. 
        How may I assist you today?"

Caller: "Hi, I'd like to look up my reservation."

Agent: "I'd be happy to help you with that. Could you please 
        provide your confirmation number?"

Caller: "It's GH-78432"

Agent: "Thank you. And may I have the last name on the reservation?"

Caller: "Smith"

Agent: [Executes lookup_reservation function]
       "I found your reservation, Mr. Smith. You have a Deluxe Ocean 
        View room booked for January 15th through January 17th. 
        Is there anything you'd like to modify?"
```

## 🛠️ Technologies Used

- **Python** - Async WebSocket server
- **Deepgram** - Speech-to-Speech API with function calling
- **Twilio** - Phone call handling and audio streaming
- **WebSockets** - Real-time bidirectional communication
- **asyncio** - Concurrent audio stream handling

## 📝 License

MIT License - feel free to use this project for learning and development.

## 🙏 Acknowledgments

- [Deepgram](https://deepgram.com/) for the Voice Agent API
- [Twilio](https://www.twilio.com/) for telephony infrastructure
