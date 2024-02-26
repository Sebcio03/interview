import React from "react";
import styles from "./Calculator.module.css";
import { Calculator } from "../../components/Calculator/Calculator.jsx";

export const CalculatorPage = () => {
  return (
    <main>
      <div className={styles.container}>
        <h1>Calculator Challenge</h1>
        <Calculator />
      </div>
    </main>
  );
};
