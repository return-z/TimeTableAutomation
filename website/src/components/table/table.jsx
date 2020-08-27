import React, { Component } from 'react';
import timetable from './timetable.json'

const days = 7;
const hours = 13;

class Table extends Component {
  constructor(props) {
    super(props);
    this.dayMap = {
      1: "Monday",
      2: "Tuesday",
      3: "Wednesday",
      4: "Thursday",
      5: "Friday",
      6: "Saturday",
    };
  }

  state = {
    grid: Array.from({ length: days }).map(() =>
      Array.from({ length: hours }).fill(0)
    ),
  };

  render() {
    return (
      <div
        style={{
          justifyContent: "center",
          marginTop: 100,
          display: "grid",
          gridTemplateColumns: `repeat(${hours}, 100px)`,
          textAlign: "center",
          alignContent: "center",
        }}
      >
        {this.state.grid.map((rows, i) =>
          rows.map((cols, j) => {
            console.log(this.dayMap[i]);
            if (i === 0 && j === 0) {
              return (
                <div />
              );
            }
            else if (j === 0 && i !== 0) {
              return (
                <div style={{width: 100,height: 50,border: "solid 1px black",alignContent: "center",backgroundColor: "#20e6dc",}}>
                  {this.dayMap[i]}
                </div>
              );
            } else if (i === 0 && j !== 0) {
              return (
                <div style={{width: 100,height: 50,border: "solid 1px black", backgroundColor: "#e89352",}}>
                  {j}
                </div>
              );
            }
            return (
              <div style={{width: 100,height: 50,border: "solid 1px black",}}>
                {timetable[i][j][0]}
              </div>
            );
          }))}
      </div>
    );
  }
}

export default Table;