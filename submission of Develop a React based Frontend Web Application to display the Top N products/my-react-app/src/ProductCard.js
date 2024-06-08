import React from 'react';
import { Link } from 'react-router-dom';

function ProductCard({ product }) {
  return (
    <div>
      {}
      <Link to={`/product/${product.id}`}>
        {}
        <img src={product.image} alt={product.name} />
        <h3>{product.name}</h3>
        <p>Price: ${product.price}</p>
        {}
      </Link>
    </div>
  );
}

export default ProductCard;