console.log("App loaded!");

import React, { useState } from "react";
import Avatar from "./Avatar";
import ClothesOverlay from "./ClothesOverlay";

function App() {
  const [height, setHeight] = useState(110); // cm
  const [weight, setWeight] = useState(20); // kg
  const [clothes, setClothes] = useState({
    length: 50, // 총길이
    chest: 35, // 가슴단면
    shoulder: 28, // 어깨너비
  });

  return (
    <div style={{ maxWidth: 400, margin: "40px auto", fontFamily: "sans-serif" }}>
      <h2>아이 아바타 & 옷 사이즈 시뮬레이터</h2>
      <div style={{ marginBottom: 16 }}>
        <label>
          키(cm):
          <input type="number" value={height} onChange={e => setHeight(Number(e.target.value))} style={{ width: 60, marginLeft: 8 }} />
        </label>
        <label style={{ marginLeft: 16 }}>
          몸무게(kg):
          <input type="number" value={weight} onChange={e => setWeight(Number(e.target.value))} style={{ width: 60, marginLeft: 8 }} />
        </label>
      </div>
      <div style={{ marginBottom: 16 }}>
        <label>
          총길이(cm):
          <input type="number" value={clothes.length} onChange={e => setClothes({ ...clothes, length: Number(e.target.value) })} style={{ width: 60, marginLeft: 8 }} />
        </label>
        <label style={{ marginLeft: 8 }}>
          가슴단면(cm):
          <input type="number" value={clothes.chest} onChange={e => setClothes({ ...clothes, chest: Number(e.target.value) })} style={{ width: 60, marginLeft: 8 }} />
        </label>
        <label style={{ marginLeft: 8 }}>
          어깨너비(cm):
          <input type="number" value={clothes.shoulder} onChange={e => setClothes({ ...clothes, shoulder: Number(e.target.value) })} style={{ width: 60, marginLeft: 8 }} />
        </label>
      </div>
      <div style={{ border: "1px solid #eee", borderRadius: 8, background: "#fafaff", padding: 16 }}>
        <svg width={220} height={320}>
          <Avatar height={height} weight={weight} />
          <ClothesOverlay height={height} clothes={clothes} />
        </svg>
      </div>
    </div>
  );
}

export default App;

