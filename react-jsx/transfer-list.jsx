import { useState, useEffect } from "react";

export function ListOfItem({ listOfItem, side, handleCheckedElement }) {
  return (
    <ul>
      {listOfItem.map(({ name, isChecked }) => (
        <>
          <input
            type="checkbox"
            key={`name-${name}-1`}
            onChange={(e) => {
              handleCheckedElement(e, side);
            }}
            name={name}
            checked={isChecked}
          />
          <li key={`li-${name}-2`}>{name}</li>
        </>
      ))}
    </ul>
  );
}

export default function App() {
  const [leftSide, setLeftSide] = useState([
    { isChecked: false, name: "HTML" },
    { isChecked: false, name: "Javascript" },
    { isChecked: false, name: "CSS" },
    { isChecked: false, name: "Typescript" },
  ]);
  const [rightSide, setRightSide] = useState([
    { isChecked: false, name: "React" },
    { isChecked: false, name: "Angular" },
    { isChecked: false, name: "Vue" },
    { isChecked: false, name: "Svelte" },
  ]);

  const moveAll = (move) => {
    let newLeftSide = [];
    let newRightSide = [];
    if (move === "left") {
      newLeftSide = [...leftSide, ...rightSide];
    } else if (move === "right") {
      newRightSide = [...rightSide, ...leftSide];
    }
    setLeftSide(newLeftSide);
    setRightSide(newRightSide);
  };

  const handleCheckedElement = (e, side) => {
    const listOfElements = side === "left" ? leftSide : rightSide;
    for (const elem of listOfElements.values()) {
      if (elem.name == e.target.name) {
        elem.isChecked = !elem.isChecked;
      }
    }
    side === "left"
      ? setLeftSide([...listOfElements])
      : setRightSide([...listOfElements]);
  };

  const move = (side) => {
    const moveItem = [];
    const stayItem = [];

    const listOfElements = side === "left" ? rightSide : leftSide;
    for (const elem of listOfElements.values()) {
      if (elem.isChecked) {
        moveItem.push(elem);
      } else {
        stayItem.push(elem);
      }
      console.log(moveItem);
      console.log(stayItem);
      if (side === "left") {
        setLeftSide([...leftSide, ...moveItem]);
        setRightSide([...stayItem]);
      } else {
        setLeftSide([...stayItem]);
        setRightSide([...rightSide, ...moveItem]);
      }
    }
  };

  return (
    <div>
      <div>
        <ListOfItem
          listOfItem={leftSide}
          side={"left"}
          handleCheckedElement={handleCheckedElement}
        />
        <button onClick={() => moveAll("left")}> Move All Left </button>
        <button onClick={() => move("left")}> Move Left </button>
        <button onClick={() => move("right")}> Move Right </button>
        <button onClick={() => moveAll("right")}> Move All Right </button>
        <ListOfItem
          listOfItem={rightSide}
          side={"right"}
          handleCheckedElement={handleCheckedElement}
        />
      </div>
    </div>
  );
}
