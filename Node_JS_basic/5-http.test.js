const request = require('supertest');
const app = require('./5-http');

describe('More complex HTTP server using node', () => {
  describe('When the database is not available', () => {
    it('Returns the right error message', (done) => {
      request(app)
        .get('/students')
        .expect(500)
        .expect('Content-Type', /text\/plain/)
        .expect('This is the list of our students\nCannot load the database', done);
    });
  });
});