#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmEndPoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let people = [];

const requestCharacters = () => {
  return new Promise((resolve, reject) => {
    request(filmEndPoint, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        reject('Error fetching movie data. StatusCode: ' + res.statusCode);
      } else {
        const jsonBody = JSON.parse(body);
        people = jsonBody.characters;
        resolve();
      }
    });
  });
};

const requestNames = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        reject('Error fetching character data. StatusCode: ' + res.statusCode);
      } else {
        const jsonBody = JSON.parse(body);
        console.log(jsonBody.name);
        resolve();
      }
    });
  });
};

const getCharacterNames = async () => {
  try {
    await requestCharacters();
    for (const characterUrl of people) {
      await requestNames(characterUrl);
    }
  } catch (error) {
    console.error(error);
  }
};

getCharacterNames();