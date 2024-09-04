#!/usr/bin/node

/**
 * script that prints all characters of a Star Wars movie using API
 * usage: ./0-starwars_characters.js <filmId>
 */

const request = require('request');

const filmId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
const peopleUrl = 'https://swapi-api.alx-tools.com/api/people/';

async function fetchData () {
  try {
    const response = await new Promise((resolve, reject) => {
      request(filmUrl, (err, res, body) => {
        if (err) reject(err);
        else resolve(body);
      });
    });

    const filmData = JSON.parse(response);
    const characters = filmData.characters;
    const peopleList = characters.map(url => url.match(/\/people\/(\d+)\//)[1]);

    const namesList = await Promise.all(
      peopleList.map(id => {
        return new Promise((resolve, reject) => {
          request(`${peopleUrl}${id}`, (err, res, body) => {
            if (err) {
              console.log(err);
              resolve(null);
            } else {
              try {
                const Data = JSON.parse(body);
                resolve(Data.name);
              } catch (err) {
                console.log(err);
                resolve(null);
              }
            }
          });
        });
      })
    );

    console.log((namesList.filter(name => name !== null)).join('\n'));
  } catch (err) {
    console.log(err);
  }
}

fetchData();
