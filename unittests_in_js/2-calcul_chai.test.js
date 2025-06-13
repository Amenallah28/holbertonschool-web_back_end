var chai = require('chai');

const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function () {
  describe('SUM no Round', function () {
    it('should return 5', function () {
      chai.expect(calculateNumber('SUM', 1, 4)).to.equal(5);
    });
  });
});