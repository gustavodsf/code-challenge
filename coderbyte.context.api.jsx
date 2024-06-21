import React, { useState, createContext, useContext } from 'react';
import { createRoot } from 'react-dom/client';

const languages = ['JavaScript', 'Python'];

const languageContext = createContext({
  language: languages[0],
  setLanguage: () => {},
})

function MainSection() {
  const { language, setLanguage } = useContext(languageContext);

  const changeLanguage = () => {
    const idx = languages.indexOf(language);
    const newLanguage = idx ? languages[0] : languages[1];
    setLanguage(newLanguage)
  }


  return (
    <div>
      <p id="favoriteLanguage">favorite programing language: {language}</p>
      <button id="changeFavorite"
        onClick={changeLanguage}
      >toggle language</button>
    </div>
  )
}

function App() {
  const [ language, setLanguage ] = useState(languages[0]) 
  return (
    <languageContext.Provider value={{ language, setLanguage }}>
      <MainSection />
    </languageContext.Provider>  
  );
}