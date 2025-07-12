import { useState } from 'react'
import './App.css';
import { Button } from '@ui/button';
import { Checkbox } from '@ui/checkbox';

function App() {

  return (
    <div className='mx-auto max-w-2xl p-4'>
      <div>
        <Button variant="primary">Primary Button</Button>
      </div>
      <div className='mt-4'>
        <Checkbox>Secondary Checkbox</Checkbox>
      </div>
    </div>
  )
}

export default App
