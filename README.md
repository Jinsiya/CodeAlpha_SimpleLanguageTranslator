# 🌍 AI Translator

An intelligent, multi-language translation application with voice output and translation history. Built with Streamlit, it supports 8+ Indian and international languages with a modern glass-morphism UI.

## 📋 Overview

AI Translator is a powerful web application that provides instant text translation between multiple languages. It features a sleek, modern interface with real-time translation, text-to-speech output, copy functionality, and a complete translation history.

## ✨ Features

### Core Features
- **Instant Translation** - Translate text between 8+ languages
- **Voice Output** - Listen to translations with text-to-speech
- **Copy to Clipboard** - One-click copy of translated text
- **Translation History** - Automatically saves all translations
- **Multi-Language Support** - French, Spanish, German, Arabic, Hindi, Tamil, Telugu, Malayalam

### UI Features
- **Glass-morphism Design** - Modern, translucent UI with blur effects
- **Dark Theme** - Eye-friendly dark mode
- **Responsive Layout** - Works on desktop and mobile
- **Animated Elements** - Smooth hover and transition effects
- **Toast Notifications** - User feedback for actions
- **Clean Typography** - Professional font styling

### Technical Features
- **Auto Language Detection** - Automatically detects source language
- **Error Handling** - Graceful error recovery
- **Persistent History** - JSON-based storage
- **Optimized Performance** - Fast and responsive

## 🛠 Technologies

| Category | Technologies |
|----------|--------------|
| **Framework** | Streamlit |
| **Translation** | deep-translator (Google Translate) |
| **Text-to-Speech** | gTTS (Google Text-to-Speech) |
| **Data Storage** | JSON |
| **UI** | HTML5, CSS3, Custom Styling |
| **Icons** | Unicode Emojis |

Translation Pipeline
text
Text Input → Language Selection → deep-translator API → Translation Display → Voice Output
User Input - Text entered in the text area

Language Selection - User selects target language

Translation - deep-translator sends request to Google Translate

Display - Translation shown in styled container

Voice Output - gTTS generates audio file

History - Translation saved to JSON file
